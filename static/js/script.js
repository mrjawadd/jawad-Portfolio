const typedText = document.querySelector(".typing");
const words = ["a Software Developer.", "a Machine Learning Enthusiast.", "a Python Developer.", "a Problem Solver."];
let wordIndex = 0;
let charIndex = 0;
let currentWord = "";
let isDeleting = false;

function type() {
    currentWord = words[wordIndex];
    if (isDeleting) {
        charIndex--;
    } else {
        charIndex++;
    }

    typedText.textContent = currentWord.substring(0, charIndex);

    let typingSpeed = isDeleting ? 60 : 120;
    if (!isDeleting && charIndex === currentWord.length) {
        typingSpeed = 1500;
        isDeleting = true;
    } else if (isDeleting && charIndex === 0) {
        isDeleting = false;
        wordIndex = (wordIndex + 1) % words.length;
        typingSpeed = 500;
    }

    setTimeout(type, typingSpeed);
}

document.addEventListener("DOMContentLoaded", type);
