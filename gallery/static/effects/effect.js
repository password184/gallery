function aos_init() {
  AOS.init({
    duration: 800,
    easing: "slide",
    once: false,
    mirrow: false,
  });
}

window.addEventListener("load", () => {
  aos_init();
});

// const navEL = document.querySelector(".navbar");
// window.addEventListener("scroll", () => {
//   if (window.scrollY >= 56) {
//     navEL.classList.add("navbar-scrolled");
//   } else if (window.scrollY < 56) {
//     navEL.classList.remove("navbar-scrolled");
//   }
// });

document.querySelectorAll(".row img").forEach((img_fluid) => {
  img_fluid.onclick = () => {
    document.querySelector(".popup-image").style.display = "block";
    document.querySelector(".popup-image img").src =
      img_fluid.getAttribute("src");
  };
});

document.querySelector(".popup-image span").onclick = () => {
  document.querySelector(".popup-image").style.display = "none";
};

window.setTimeout(function () {
  $(".alert")
    .fadeTo(500, 0)
    .slideUp(500, function () {
      $(this).remove();
    });
}, 4000);
