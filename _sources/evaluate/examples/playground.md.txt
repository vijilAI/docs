# Playground

Vijil offers a playground on which you can test select red-teaming prompts on an agent of your choice.

Visit it by clicking on **Playground** in the left sidebar.

Playground Chat is a regular chat interface where you can start conversations with one or more models. You can have multiple conversations side-by-side and compare the responses from different models.

Playground Snapshot is a way to get one-off responses from one or more models to a single prompt, and compare their responses side-by-side.

## Playground Chat

1. Select one or more [agents](agents.md) that you want to "play" with, or click **Add Agent** to add a new agent.
2. In the Playground Chat section, enter your user message. Some agent APIs let you submit a conversation with prepopulated agent responses. If this is something you want, you can use the **Assistant** option to populate previous agent responses. Switch back to **User** to add user messages.

## Playground Snapshot

1. Select one or more [agents](agents.md) that you want to "play" with, or click **Add Agent** to add a new agent.
2. Next, select the prompt you want to start with. In **Search Prompts**, we offer a selection of red-teaming prompts that you can use to test your agent. Copy one of those propmts and enter it into the **Base Prompt** section of **Mutate Prompts**. Alternatively, you can write your own prompt in the **Base Prompt** section.
3. Optionally, make your prompt more adversarial by mutating the base prompt with an attack. Under **Attackers**, select one or more of the attack techniques available.
4. Click **Run Snapshot** to get responses from the selected agents.
5. View the responses side-by-side in the **Playground Snapshot** section.