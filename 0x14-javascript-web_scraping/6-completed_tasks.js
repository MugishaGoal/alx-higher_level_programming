#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const tasks = JSON.parse(body);
    const completedTasks = {};

    tasks.forEach(task => {
      if (task.completed) {
        const userId = task.userId.toString();
        if (completedTasks[userId]) {
          completedTasks[userId]++;
        } else {
          completedTasks[userId] = 1;
        }
      }
    });

    console.log(completedTasks);
  } else {
    console.error('Error:', error);
  }
});
