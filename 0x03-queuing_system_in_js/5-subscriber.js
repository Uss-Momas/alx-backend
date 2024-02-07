import { createClient } from 'redis';

const client = createClient()

client.on('error', err => console.log(`Redis client not connected to the server: ${err.toString()}`));

client.on('connect', () => console.log('Redis client connected to the server'));

const listener = (channel, message) => {
  if (channel === 'holberton school channel') {
    if (message === 'KILL_SERVER') {
      client.unsubscribe(channel);
      client.quit();
    }
    console.log(message);
  }
};
client.subscribe('holberton school channel');

client.on('message', listener);