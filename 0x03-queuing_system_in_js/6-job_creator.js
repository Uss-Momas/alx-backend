const kue = require('kue');

const queue = kue.createQueue();

const object = {
  phoneNumber: '+258861234567',
  message: 'Verify your number!',
}
const job = queue.create('push_notification_code', object).save((err) => { if (!err) console.log(`Notification job created: ${job.id}`) });

job.on('complete', (result) => { console.log('Notification job completed') });

job.on('failed', (err) => { console.log('Notification job failed') });

