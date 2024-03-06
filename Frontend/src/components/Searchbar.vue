<template>
  <div class="pt-4 w-screen flex flex-col items-center justify-center">
    <!-- Add the @submit.prevent to listen for the submit event and prevent the default form submission behavior -->
    <form @submit.prevent="handleSubmit" class=" w-7/12">
      <input type="text" id="question"
        class="text-gray-900 border border-gray-300 text-sm rounded-lg focus:ring-violet-700 focus:border-violet-700 block w-full p-2.5 bg-violet-300 placeholder-gray-700"
        placeholder="Ask a question!" required />
      <!-- Optional: Add a submit button if you want a clickable option in addition to pressing Enter -->
      <!-- <button type="submit" class="mt-2">Submit</button> -->
    </form>

    <!-- Display the API call response here -->
    <div v-if="serverResponse" class="mt-4 mx-8 p-4 border border-gray-300 rounded-lg bg-gray-100">
      {{ serverResponse }}
    </div>
    <div v-if="loading" class="loading-message">Loading...</div>

    <!-- <VueTyper text="hiiii"></VueTyper> -->
  </div>
</template>

<script setup>
  import { ref } from 'vue';
  import { VueTyper } from 'vue-typer'

  // Define a reactive property to hold the question entered by the user
  const question = ref('');
  
  // Define a reactive property to hold the server response
  const serverResponse = ref('');

  const loading = ref(false);

  // Define a method to handle form submission
  async function handleSubmit() {
  loading.value = true;
  try {
    const inputBox = document.getElementById('question'); // Assuming the input box has the id 'first_name'
    const questionContent = inputBox.value;

    const response = await fetch('http://127.0.0.1:5000/askQuestion', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ question: questionContent })
    });

    const data = await response.text(); // Assuming the response is text
    console.log('Response from server:', data);
    // Set the server response to be displayed in the box
    serverResponse.value = data;
  } catch (error) {
    console.error('Error:', error);
    serverResponse.value = 'An error occurred. Please try again.';
  } finally {
    loading.value = false;
  }
}
</script>


<style scoped>
/* Additional styles if needed */
</style>