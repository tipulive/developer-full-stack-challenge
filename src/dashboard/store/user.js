export const state = () => ({
    UserData: [],
    errorData:[],
    isLoggedIn:false,



  });

  export const mutations = {
    SET_USER(state, UserData) {
      state.UserData = UserData;
    },
    SET_ERROR(state,errorData) {
        state.errorData =errorData;
      },
      update_login(state,isLoggedIn)
      {
        state.isLoggedIn=isLoggedIn;
      }
  };

  export const actions = {

    async registerUser({ commit },payload) {

       //const { name,author_id,pages } = payload;
         // Fetch books from the API
          await this.$axios.post('/register', payload)
            .then((response) => {

                const result = response.data;
                commit('SET_USER',result);
            })
            .catch((error) => {

                commit('SET_ERROR',error);
            });


      },
      async LoginUser({ commit },payload) {

        await this.$axios.post('/login', payload)
        .then((response) => {

            const result = response.data;
            commit('SET_USER',result);
        })
        .catch((error) => {

            commit('SET_ERROR',error);
        });



      },
      async Logout({ commit },payload) {
         await this.$axios.post('/logout', payload)
            .then((response) => {

                localStorage.removeItem(process.env.TOKEN_KEY);
            })
            .catch((error) => {

                commit('SET_ERROR',error);
            });

      }
  };
