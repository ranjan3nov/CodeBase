<script setup>
import JobCard from '@/components/JobCard.vue';
import { reactive, defineProps, onMounted } from 'vue';
import { RouterLink } from 'vue-router';
import axios from 'axios';
import PulseLoader from 'vue-spinner/src/PulseLoader.vue';

defineProps({
  limit: Number,
  showButton: {
    type: Boolean,
    default: true,
  }
})
const state = reactive({
  jobs: [],
  isLoading: true
});

onMounted( async ()=>{
  try {
    const res = await axios.get('/api/jobs');
    state.jobs = res.data;
  } catch (error) {
    console.log(error);
  } finally{
    state.isLoading = false;
  }
})

</script>

<template>
  <section class="bg-blue-50 px-4 py-10">
    <div class="container-xl lg:container m-auto">
      <h2 class="text-3xl font-bold text-blue-500 mb-6 text-center">
        Browse Jobs
      </h2>
      <!-- Show Loading Spinner while loading is true -->
       <div v-if="state.isLoading" class="text-center text-gray-500">
          <PulseLoader />
       </div>
       <!-- Show the jobs while loading is flase  -->
      <div v-else class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <JobCard v-for="job in state.jobs.slice(0, limit || state.jobs.length)" :key="job.id" :job="job" />
      </div>
    </div>
  </section>

  <section v-if="showButton" class="m-auto max-w-lg my-10 px-6">
    <RouterLink to="/jobs" class="block bg-black text-white text-center py-4 px-6 rounded-xl hover:bg-gray-700">
      View All Jobs
    </RouterLink>
  </section>

</template>