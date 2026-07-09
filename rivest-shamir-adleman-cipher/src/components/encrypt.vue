<template>
  <body>
    <div class="row">
      <h1>Recipient:</h1>
      <input type="text">
    </div>

    <div class="row">
      <h1>Message:</h1>
      <textarea></textarea>
    </div>

    <div class="row">
      <button class="button">Encrypt!</button>
    </div>

    <div class="row">
      <h2>Status Message</h2>
    </div>
  </body>
</template>

<style scoped>
  body {
    margin-top: 15vh;
    margin-bottom: 3vh;
    
    display: flex;
    justify-content: center;
    align-items: center;

    min-height: 100vh;

    display: flex;
    flex-direction: column;

    gap: 15vh;

    align-items: center;

    .row {
      display: flex;
      flex-direction: row;
      align-items: center;
      justify-content: center;

      gap: 10vw;

      width: 40vw;

      input {
        height: 100%;
        width: 20vw;

        font-size: 130%;
      }

      textarea {
        max-width: 80vw;
      }

      button {
        width: 10vw;
        height: 5vh;
      }
    }
  }
</style>