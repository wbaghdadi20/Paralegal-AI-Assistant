import { createRouter, createWebHistory } from 'vue-router';
import Homepage from '../views/Homepage.vue'; // Import the ContactPage component

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'homepage',
      component: Homepage // Set ContactPage as the default route
    }
    // Add other routes as needed
  ]
});

export default router;
