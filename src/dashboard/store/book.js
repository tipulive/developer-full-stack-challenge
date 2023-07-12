export const state = () => ({
    bookData: [],
    BookPass:[],
  });

  export const mutations = {
    SET_bookS(state, bookData) {
      state.bookData = bookData;
    },
    updateBPass(state, BookPass) {
        state.BookPass = BookPass;
      }
  };

  export const actions = {
    async updateBookPass({ commit },payload) {
        commit('updateBPass',payload);
      },
    async fetchBooks({ commit },payload) {
        try {
            const { page, limit,search,sort} = payload;
          // Fetch books from the API
          var token=localStorage.getItem(process.env.TOKEN_KEY);
          this.$axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
          const response = await this.$axios.get(`/books_paginate?page=${page}&limit=${limit}&search=${search}&sort=${sort}`);
          const books = response.data.books;
          commit('SET_bookS',books);
        } catch (error) {
          console.error(error);
        }
      },
      async addBooks({ commit },payload) {

            //const { name,author_id,pages } = payload;
          // Fetch books from the API
          var token=localStorage.getItem(process.env.TOKEN_KEY);
          this.$axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
          await this.$axios.post('/books', payload)
            .then((response) => {

              console.log(response);
            })
            .catch((error) => {
              console.log(error);
            });

      },
      async editBook({ dispatch },payload) {
        const {id} = payload;
        var token=localStorage.getItem(process.env.TOKEN_KEY);
        this.$axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
        this.$axios.put(`/books/${id}`,payload)
            .then((response) => {
                const payloadData = {
                    page:1,
                    limit:10,
                    search:"",
                    sort:"asc"
                  };
                dispatch('fetchBooks',payloadData);
              console.log(response);
            })
            .catch((error) => {
              console.log(error);
            });

      }
  };
