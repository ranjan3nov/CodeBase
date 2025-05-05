import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import NotFoundView from '@/views/NotFoundView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: HomeView,
    },
    {
        path: '/jobs',
        name: 'Jobs',
        component: () => import('@/views/JobsView.vue'),
    },
    {
      path:'/:catchAll(.*)',
      name: 'NotFound',
      component: NotFoundView,
    }
  ],
})

export default router