{
  description = "Discord bot that responds random nikuman image";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    treefmt-nix = {
      url = "github:numtide/treefmt-nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
    devshell = {
      url = "github:numtide/devshell";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs = inputs @ {flake-parts, ...}:
    flake-parts.lib.mkFlake {inherit inputs;} {
      systems = ["x86_64-linux" "aarch64-linux" "aarch64-darwin" "x86_64-darwin"];
      imports = [inputs.devshell.flakeModule inputs.treefmt-nix.flakeModule];
      perSystem = {
        config,
        self',
        inputs',
        pkgs,
        system,
        ...
      }: let
        pyPkgs = pythonPackages:
          with pythonPackages; [
            black
            pyflakes
            isort
            pytest
            nose
            # Dependencies ⇓⇓⇓⇓⇓
            discordpy
          ];
        nikuman-gacha = with pkgs;
          stdenv.mkDerivation {
            name = "nikuman-gacha";
            propagatedBuildInputs = [(python3.withPackages pyPkgs)];
            dontUnpack = true;
            installPhase = "install -Dm755 ${./main.py} $out/bin/nikuman-gacha";
          };
      in {
        devshells.default = {
          packages = with pkgs; [config.treefmt.build.wrapper (python3.withPackages pyPkgs) nodePackages_latest.pyright];
        };
        treefmt = {
          # Nix formatter
          programs.alejandra.enable = true;
          # Python formatter
          programs.black.enable = true;
          flakeFormatter = true;
          projectRootFile = "flake.nix";
        };
        packages.default = nikuman-gacha;
      };
    };
}
