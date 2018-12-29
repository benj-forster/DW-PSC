const DW = require('DW');
const DWClient = new DW(`${client.user.id}`, 'TOKEN_HERE');

DWCLIENT.updateCount(client.guilds.size).then(() => {
    console.log('Server Count Posted!')
}).catch((e) => {
    console.error(e)
})
