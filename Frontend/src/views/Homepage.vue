<template>
    <div class="contact-page">
      <h1 class="title">Talk to us</h1>
      <div class="search-bar-container">
        <input
          type="text"
          v-model="searchQuery"
          @keyup.enter="onSearch"
          placeholder="Enter your query..."
          class="search-bar"
        />
      </div>
  
      <div v-if="conversation.length > 0" class="conversation">
        <div v-for="(message, index) in conversation" :key="index" class="message-container">
          <div :class="{'user-message': message.sender === 'user', 'bot-message': message.sender === 'bot'}">
            <span :class="{'user-dot': message.sender === 'user', 'bot-dot': message.sender === 'bot'}"></span>
            {{ message.content }}
          </div>
        </div>
        <button @click="clearConversation" class="clear-button">Clear</button>
      </div>
    </div>
  </template>
  
  
  <script>
  export default {
    data() {
      return {
        searchQuery: '',
        conversation: [],
      };
    },
    methods: {
      onSearch() {
        this.conversation.push({ content: this.searchQuery, sender: 'user' });
        if (this.searchQuery.toLowerCase().includes('hello')) {
          this.conversation.push({ content: "1. Task1 2. Task2", sender: 'bot' });
        }
        this.searchQuery = '';
      },
      clearConversation() {
        this.conversation = [];
      },
    },
  };
  </script>
  
  
  <style>
  .contact-page {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
  }
  
  .title {
    font-size: 32px;
    margin-bottom: 20px;
    text-align: center;
  }
  
  .search-bar-container {
    width: 100%;
    max-width: 500px;
  }
  
  .search-bar {
    width: 100%;
    padding: 12px 15px;
    font-size: 16px;
    border: 2px solid #ddd;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    margin-bottom: 20px;
  }
  
  .conversation {
    width: 100%;
    max-width: 500px;
    border: 2px solid #ddd;
    border-radius: 8px;
    padding: 10px;
    overflow-y: auto;
    background-color: #fafafa;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  
  .user-message {
    align-self: flex-end;
    background-color: #e0e0e0;
    padding: 8px 10px;
    border-radius: 10px;
    margin-bottom: 5px;
    word-wrap: break-word;
  }
  
  .bot-message {
    align-self: flex-start;
    background-color: #f0f0f0;
    padding: 8px 10px;
    border-radius: 10px;
    margin-top: 5px;
    word-wrap: break-word;
  }
  
  .clear-button {
    padding: 8px 15px;
    margin-top: 10px;
    background-color: #f44336;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  .clear-button:hover {
    background-color: #d32f2f;
  }
  </style>
  