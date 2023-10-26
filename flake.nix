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
            discordpy
            black
            pyflakes
            isort
            pytest
            nose
          ];
      in {
        devshells.default = {
          packages = with pkgs; [config.treefmt.build.wrapper (python3.withPackages pyPkgs) nodePackages_latest.pyright];
        };
        treefmt = {
          programs.alejandra.enable = true;
          programs.black.enable = true;
          flakeFormatter = true;
          projectRootFile = "flake.nix";
        };
      };
    };
}
