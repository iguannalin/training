1. Open the Navigate menu.
1. Select `Campaigns > agents`.
1. Press the button to deploy an agent.
1. Choose Manx agent.
1. Choose Linux platform.
1. Update the `app.contact.http` value to specify an ip address of `127.0.0.1` (keep the port). This is for downloading the agent binary.
1. Update the `app.contact.tcp` value to specify an ip address of `127.0.0.1` (keep the port). This is for the agent-C2 communication channel.
1. Select and copy the first command to your clipboard. This command will instruct the agent to communicate over a TCP channel.
1. On your local system and outside of CALDERA, open a shell in a terminal.
1. Paste the copied command and execute it.
1. Wait for the agent to appear in the agent table.
1. Task completed.