import { createRouter, createWebHistory } from 'vue-router';
import Homepage from '../views/Homepage.vue';
import ConversationPage from '../views/ConversationPage.vue';
import Login from '../views/Login.vue'; 
import NewConversationPage from '../views/NewConversationPage.vue';

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
    },
    {
      path: '/newconversation',
      name: 'Newconversation',
      component: NewConversationPage // Make sure to create this component
    },
  ]
});

export default router;
