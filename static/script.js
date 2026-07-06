// Footer year
const yearEl = document.getElementById("year");
if (yearEl) yearEl.textContent = new Date().getFullYear();

// Gentle reveal for catalog entries as they scroll into view
if ("IntersectionObserver" in window) {
  const entries = document.querySelectorAll(".entry");
  entries.forEach((el) => {
    el.style.opacity = 0;
    el.style.transform = "translateY(8px)";
    el.style.transition = "opacity 0.5s ease, transform 0.5s ease";
  });

  const observer = new IntersectionObserver(
    (observed) => {
      observed.forEach((item) => {
        if (item.isIntersecting) {
          item.target.style.opacity = 1;
          item.target.style.transform = "translateY(0)";
          observer.unobserve(item.target);
        }
      });
    },
    { threshold: 0.15 }
  );

  entries.forEach((el) => observer.observe(el));
}
