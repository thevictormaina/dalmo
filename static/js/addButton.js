let button = document.querySelector("#addButton");
let overlay = document.getElementById('addOverlay');

function toggleOverlay(){
    console.log(button)
    // Toggle button rotation
    if(button.classList.contains('clicked')){
        // Off
        button.classList.remove('clicked');
        overlay.classList.remove('overlayActive');
    } else {
        // On
        button.classList.add('clicked');
        overlay.classList.add('overlayActive');
    }
}


button.addEventListener('click', ()=>{
    toggleOverlay();
})
overlay.addEventListener('click', ()=>{
    toggleOverlay();
})