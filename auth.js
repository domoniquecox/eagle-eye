/*const ui = new firebaseui.auth.AuthUI(firebase.auth());

const uiConfig = {

  callbacks: {
    signInSuccessWithAuthResult(authResult, redirectUrl){
        console.log("Success!");
      return true;
    },



    firebase.auth().onAuthStateChanged(user => {
  if(user) {
    window.location = 'index.html'; //After successful login, user will be redirected to home.html
}
}

    uiShown() {
      document.getElementById('loader').style.display = 'none';
    },
  },
  signInFlow: 'popup',
  signInSuccessUrl: 'signedIn',
  signInOptions: [
    firebase.auth.EmailAuthProvider.PROVIDER_ID,
    //firebase.auth.GoogleAuthProvider.PROVIDER_ID,
  ],
};
ui.start('#firebaseui-auth-container', uiConfig);

*/




const ui = new firebaseui.auth.AuthUI(firebase.auth());

const uiConfig = {
 callbacks: {
   signInSuccessWithAuthResult(authResult, redirectUrl) {
     return true;

/*
firebase.auth().onAuthStateChanged(function(user)){
if(user) {
window.location = 'courses.html'; //After successful login, user will be redirected to courses.html
}
}
*/


   },
   uiShown() {
     document.getElementById('loader').style.display = 'none';
   },
 },
 signInFlow: 'popup',
 //signInSuccessUrl: 'signedIn',
 signInSuccessUrl: 'courses.html',
 signInOptions: [
   firebase.auth.EmailAuthProvider.PROVIDER_ID,
   //firebase.auth.GoogleAuthProvider.PROVIDER_ID,
 ],
 //window.location.href = courses.html;
};
ui.start('#firebaseui-auth-container', uiConfig);
