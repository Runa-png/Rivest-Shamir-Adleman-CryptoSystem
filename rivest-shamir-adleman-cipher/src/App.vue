<script setup></script>

<template>
  <body>
    <div class="routerBar">
      <div class="item">
        <a href="/encrypt">Encrypt</a>
      </div>
      
      <div class="item">
        <a href="/decrypt">Decrypt</a>
      </div>
    </div>
    <router-view>

    </router-view>
  </body>
</template>

<style>
  * {
    margin: 0;
  }

  .routerBar {
    display: flex;
    justify-content: space-evenly;
    align-items: center;

    position: fixed;
    top: 0;
    left: 0;

    width: 100vw;
    height: 7.5vh;

    background-color: rgba(255, 255, 255, 0.9);
  }
</style>
