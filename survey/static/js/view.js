
let next_btn1 = document.getElementById("next_btn1");
next_btn1.addEventListener("click", enableForm2);

let next_btn2 = document.getElementById("next_btn2");
next_btn2.addEventListener("click", enableForm3);

let next_btn3 = document.getElementById("next_btn3");
next_btn3.addEventListener("click", enableForm4);

let next_btn4 = document.getElementById("next_btn4");
next_btn4.addEventListener("click", enableForm5);

function enableForm2() {
    try {
    // Function to  Disable first_name & Enable last_name
    let first_name = document.getElementById("first_name_block");
    first_name.classList.add("hide_this_div");

    let last_name = document.getElementById("last_name_block");
    last_name.classList.remove("hide_this_div");

    // Disable 'Next 1' Button
    let next_btn1 = document.getElementById("next_btn1");
    next_btn1.classList.add("hide_this_div");

    // Enable 'Next 2' Button
    let next_btn2 = document.getElementById("next_btn2");
    next_btn2.classList.remove("hide_this_div");
    }
    catch (error) {
        console.log("Error Occured: " + error);
    }
}


function enableForm3() {
    // Function to  Disable last_name & Enable gender
    let last_name = document.getElementById("last_name_block");
    last_name.classList.add("hide_this_div");

    let gender = document.getElementById("gender_block");
    gender.classList.remove("hide_this_div");

    // Disable 'Next 2' Button
    let next_btn2 = document.getElementById("next_btn2");
    next_btn2.classList.add("hide_this_div");

    // Enable 'Next 3' Button
    let next_btn3 = document.getElementById("next_btn3");
    next_btn3.classList.remove("hide_this_div");
}

function enableForm4() {
    // Function to  Disable gender & Enable preference
    let gender = document.getElementById("gender_block");
    gender.classList.add("hide_this_div");

    let preference_block = document.getElementById("preference_block");
    preference_block.classList.remove("hide_this_div");

    // Disable 'Next 3' Button
    let next_btn3 = document.getElementById("next_btn3");
    next_btn3.classList.add("hide_this_div");

    // Enable 'Next 4' Button
    let next_btn4 = document.getElementById("next_btn4");
    next_btn4.classList.remove("hide_this_div");
}


function enableForm5() {
    // Function to  Disable preference & Enable slider
    let preference_block = document.getElementById("preference_block");
    preference_block.classList.add("hide_this_div");

    let slider_block = document.getElementById("slider_block");
    slider_block.classList.remove("hide_this_div");

    // Disable 'Next 4' Button
    let next_btn4 = document.getElementById("next_btn4");
    next_btn4.classList.add("hide_this_div");

    // Enable 'Submit' Button
    let submit_btn = document.getElementById("submit_btn");
    submit_btn.classList.remove("hide_this_div");
}