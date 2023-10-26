const {
    Client,
    EmbedBuilder,
    SlashCommandBuilder,
    AttachmentBuilder,
    GatewayIntentBits,
    Partials,
    ClientApplication,
    Routes,
    REST
} = require("discord.js");

const client = new Client ({
    intents: [Object.keys(GatewayIntentBits)],
    partials: [Partials.Message, Partials.MessageContent, Partials.Channels, Partials.Reaction]
});

const fs = require("fs");
const config = require("./config.json");

client.on("ready", async () => {
    console.log("Starting...");

    const cmd = new SlashCommandBuilder()
	    .setName("nikuman")
        .setDescription('肉まんをランダムで送信します');

    const commands = [cmd];

	console.log("Refresh SlashCommands...")
	const rest = new REST({version: "10"}).setToken(config.token)
	await rest.put(
		Routes.applicationCommands(client.user.id),
		{body: commands},
	);

    console.log("started")

});

client.on("interactionCreate", async interaction => {
    if(!interaction.isChatInputCommand()) return;

    if(interaction.commandName == "nikuman") {
        let files = fs.readdirSync("./images");
        files = files.filter(fileName=>fileName.endsWith((".png")));
        const file = files[Math.floor(Math.random() * files.length)]
        const attachment = new AttachmentBuilder("./images/"+file);
        const embed = {
            title: "肉まんガチャ",
            image: {
                url: "attachment://"+file
            },
        };
        await interaction.reply({embeds: [embed], files: [attachment]});
    };
})

client.login(config.token);
