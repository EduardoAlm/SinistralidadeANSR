<template>
  <div>
    <p>&nbsp;</p>
    <div class="w3-content w3-display-container" style="width:100%; heigth: 200%">
      <img class="mySlides" src="@/assets/img/ansr1.jpg" />
      <img class="mySlides" src="@/assets/img/ansr2.jpeg" />
      <div class="w3-center w3-display-bottommiddle" style="width:100%; heigth: 200%">
        <div class="w3-left" @click="plusDivs(-1)">&#10094;</div>
        <div class="w3-right" @click="plusDivs(1)">&#10095;</div>
        <span class="w3-badge demo w3-border" @click="currentDiv(1)"></span>
        <span class="w3-badge demo w3-border" @click="currentDiv(2)"></span>
      </div>
    </div>
  </div>
</template>


<script>
export default {
  name: "Index",
  data() {
    return {
      slideIndex: 1
    };
  },
  methods: {
    showDivs(n) {
      var i;
      var x = document.getElementsByClassName("mySlides");
      var dots = document.getElementsByClassName("demo");
      if (n > x.length) {
        this.slideIndex = 1;
      }
      if (n < 1) {
        this.slideIndex = x.length;
      }
      for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
      }
      for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" w3-white", "");
      }
      x[this.slideIndex - 1].style.display = "block";
      dots[this.slideIndex - 1].className += " w3-white";
    },
    plusDivs(n) {
      this.showDivs((this.slideIndex += n));
    },

    currentDiv(n) {
      this.showDivs((this.slideIndex = n));
    }
  },
  mounted() {
    this.showDivs(this.slideIndex);
  }
};
</script>