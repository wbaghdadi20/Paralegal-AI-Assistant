<!-- <template>
    <div class="search-container">
      <input
        type="text"
        v-model="searchQuery"
        @keyup.enter="onSearch"
        placeholder="Enter search term..."
        class="search-box"
      />
    </div>
  </template> -->
  <!-- <template>
    <div class="search-container">
      <div class="conversation">
        <div v-for="(message, index) in conversation" :key="index" :class="{'user-message': message.sender === 'user', 'bot-message': message.sender === 'bot'}">
          {{ message.content }}
        </div>
      </div>
      <input
        type="text"
        v-model="userInput"
        @keyup.enter="handleInput"
        placeholder="Type here..."
        class="search-box"
      />
    </div>
  </template> -->
  
  
  <!-- <script>
  export default {
    name: "SearchBox",
    data() {
      return {
        searchQuery: '',
      };
    },
    methods: {
      onSearch() {
        console.log("Search for:", this.searchQuery);
        // Add your search handling logic here
      },
    },
  };
  </script> -->
  
  <!-- <script>
    export default {
    name: "SearchBox",
    data() {
        return {
        userInput: '',
        conversation: [],
        };
    },
    methods: {
        handleInput() {
        this.conversation.push({ content: this.userInput, sender: 'user' });

        if (this.userInput.toLowerCase().includes('hello')) {
            this.conversation.push({ content: "1. Task1 2. Task2", sender: 'bot' });
        }

        this.userInput = '';
        }
    },
    };
    </script> -->


  <!-- <style>
  .search-container {
    display: flex;
    justify-content: center;
    margin-top: 20px;
  }
  
  .search-box {
    width: 300px;
    padding: 10px;
    font-size: 16px;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  </style> -->
  <!-- <style>
    .search-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 20px;
    }

    .conversation {
    width: 300px;
    max-height: 300px;
    overflow-y: auto;
    border: 1px solid #ccc;
    border-radius: 5px;
    padding: 10px;
    margin-bottom: 10px;
    }

    .search-box {
    width: 300px;
    padding: 10px;
    font-size: 16px;
    border: 1px solid #ccc;
    border-radius: 5px;
    }

    .user-message {
    text-align: right;
    margin: 5px;
    padding: 5px;
    background-color: #e0e0e0;
    border-radius: 10px;
    }

    .bot-message {
    text-align: left;
    margin: 5px;
    padding: 5px;
    background-color: #f0f0f0;
    border-radius: 10px;
    }
    </style> -->

  