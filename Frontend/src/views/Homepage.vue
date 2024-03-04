<template>
  
<div class="bg-gray-900 text-white w-full flex flex-col items-center justify-center h-screen">
  <Navbar/>
  <h1 class="purple1 text-4xl w-12 font-bold">Chatbot</h1>
</div>

</template>

<script>
import Navbar from '../components/Navbar.vue';

export default {
  data() {
    return {
      question: '',
      messages: [],
    };
  },
  methods: {
    async submitQuestion() {
      if (!this.question) return;

      // Simulate user message
      this.messages.push({ text: this.question, sender: 'user' });
      
      // Placeholder for your API call
      const response = await this.fetchApiResponse(this.question);
      
      // Simulate API response
      this.messages.push({ text: response, sender: 'bot' });
      
      // Clear the question input
      this.question = '';
    },
    async fetchApiResponse(question) {
      // Replace this with your actual API call
      // Example: return await axios.post('your-api-endpoint', { question });
      return new Promise((resolve) => {
        setTimeout(() => resolve(`This is a simulated response for: "${question}"`), 1000);
      });
    },
  },
};
</script>

<style scoped>
/* Additional styling can go here */
</style>
