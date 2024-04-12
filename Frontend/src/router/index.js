import { createRouter, createWebHistory } from 'vue-router';
import Homepage from '../views/Homepage.vue'; // Import the ContactPage component
import ConversationPage from '../views/ConversationPage.vue'; // This will be your new page with the table
import Login from '../views/Login.vue'; 

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'homepage',
      component: Homepage // Set ContactPage as the default route
    },
    {
      path: '/conversation',
      name: 'Conversation',
      component: ConversationPage // Make sure to create this component
    },
    {
      path: '/login',
      name: 'Login',
      component: Login // Make sure to create this component
    }
  ]
});

export default router;
