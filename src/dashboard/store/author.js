export const state = () => ({
    authorData: [],
    AuthorPass:[],



  });

  export const mutations = {
    SET_AUTHORS(state, authorData) {
      state.authorData = authorData;

    },

      updateAPass(state, AuthorPass) {
        state.AuthorPass = AuthorPass;
      }
  };

  export const actions = {
    async updateAuthorPass({ commit },payload) {
        commit('updateAPass',payload);
      },

    async fetchAuthors({ commit },payload) {
        try {
            const { page, limit,search,sort} = payload;
          // Fetch authors from the API
          var token=localStorage.getItem(process.env.TOKEN_KEY);
          this.$axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
          const response = await this.$axios.get(`/authors?page=${page}&limit=${limit}&search=${search}&sort=${sort}`);
          const authors = response.data.authors;
          commit('SET_AUTHORS',authors);
        } catch (error) {
          console.error(error);
        }
      },
      async addAuthors({ dispatch },payload) {

        //const { name,author_id,pages } = payload;
      // Fetch books from the API
      var token=localStorage.getItem(process.env.TOKEN_KEY);
      this.$axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
      await this.$axios.post('/authors', payload)
        .then((response) => {

            const payloadData = {
                page:1,
                limit:10,
                search:"",
                sort:"desc"
              };
            dispatch('fetchAuthors',payloadData);
        })
        .catch((error) => {
          console.log(error);
        });

  },


      async editAuthor({ dispatch },payload) {
        const {id} = payload;
        var token=localStorage.getItem(process.env.TOKEN_KEY);
        this.$axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
        this.$axios.put(`/authors/${id}`,payload)
            .then((response) => {
                const payloadData = {
                    page:1,
                    limit:10,
                    search:"",
                    sort:"desc"
                  };
                dispatch('fetchAuthors',payloadData);
              console.log(response);
            })
            .catch((error) => {
              console.log(error);
            });

      }
  };
