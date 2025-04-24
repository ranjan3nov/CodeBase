<script setup>

import {ref, onMounted} from 'vue';

    const name = ref('Ranjan');
    const status = ref('active');
    const tasks = ref(['task one', 'task two', 'task three']);
    const link = ref('https://google.com');

    const toggleStatus = () => {
      if (status.value === 'active') {
        status.value = 'pending';
      } else if (status.value === 'pending') {
        status.value = 'inactive';
      } else {
        status.value = 'active';
      }
    };
    const taskName = ref('');

    const addTask = () => {
      if(taskName.value.trim() !== ''){
        tasks.value.push(taskName.value);
        taskName.value = '';
      };
    };
    onMounted(async () => {
      try {
        const res = await fetch('https://jsonplaceholder.typicode.com/todos');
        const data = await res.json();
        tasks.value = data.map(task => task.title);
        console.log(data);
      } catch (error) {
        console.log(error);
      }
    });
</script>

<template>
  <h1>{{ name }}</h1>

  <p v-if="status === 'active'">
    User is active
  </p>
  <p v-else-if="status === 'pending'">
    user is pending
  </p>
  <p v-else>
    User is inactive
  </p>

  <form @submit.prevent="addTask">
    <input type="text" v-model="taskName">
    <button>Add</button>
  </form>


    <div v-for="task in tasks" :key="task">
      <span>{{ tasks.indexOf(task) + 1 }}. {{ task }}</span>
      <span> <button @click="tasks.splice(tasks.indexOf(task), 1)">X</button> </span>
    </div>


  <button @click="toggleStatus">Change Status</button>
</template>