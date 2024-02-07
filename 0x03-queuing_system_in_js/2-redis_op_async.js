import { createClient } from "redis";
import { print } from "redis";

const util = require('util');

const client = createClient();

client.on('error', (err) => { console.log(`Redis client not connected to the server: ${err.toString()}`) });

client.on('connect', () => console.log('Redis client connected to the server'));

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

async function displaySchoolValue(schoolName) {
  const get = util.promisify(client.GET).bind(client);
  return await get(schoolName);
}

displaySchoolValue('Holberton').then((value) => {console.log(value);}).catch((err) => console.log(err));
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco').then((value) => {console.log(value);});