#!/usr/bin/node
// A script that computes the number of tasks completed by user ID
const request = require('request');
const apiUrl = 'https://jsonplaceholder.typicode.com/todos';

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.log('Error:', error);
  } else {
    const tasks = JSON.parse(body);
    const completedTasksCount = {};

    tasks.forEach(task => {
      if (task.completed) {
        if (!completedTasksCount[task.userId]) {
          completedTasksCount[task.userId] = 0;
        }
        completedTasksCount[task.userId]++;
      }
    });
    console.log(completedTasksCount);
  }
});
