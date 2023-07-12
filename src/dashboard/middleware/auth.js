// middleware/jwtAuth.js

export default function ({redirect,store }) {
    // Check if the JWT token exists in the browser's localStorage or vuex state
 //console.log(process.env.API_KEY);

    var token=localStorage.getItem(process.env.TOKEN_KEY)
    //console.log(token);
 if(!token) {
    const payload=false;
    store.commit('user/update_login', payload);

    return redirect("/login")
   //console.log(store.state.user.userTest)
 }
 else{

    const payload=true;
    store.commit('user/update_login',payload);
 }

  }
