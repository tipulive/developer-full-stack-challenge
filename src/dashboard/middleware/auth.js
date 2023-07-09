// middleware/jwtAuth.js

export default function ({redirect }) {
    // Check if the JWT token exists in the browser's localStorage or vuex state
 var token=localStorage.getItem('token')
 if(!token) {
    return redirect("login")
   //console.log("test")
 }

  }
