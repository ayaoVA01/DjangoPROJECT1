// === === === == search === === ==


const navSearch = document.getElementById('nav_search'),
    div_input = document.getElementById('fa_search'),
    input_button = document.getElementById('back'),
    boxchat = document.getElementById('boxchat'),
    people_search = document.getElementById('people_search')

div_input.addEventListener('click', () => {
    navSearch.classList.add('show-search'),
        people_search.classList.add('people_search_show')

})
input_button.addEventListener('click', () => {
        navSearch.classList.remove('show-search'),
            people_search.classList.remove('people_search_show')
    })
    // === === = ... === === === ===
const navMenu = document.getElementById('nav-menu'),
    navToggle = document.getElementById('nav-toggle'),
    navClose = document.getElementById('nav-close')
navToggle.addEventListener('click', () => {
    navMenu.classList.add('show-menu')
})

navToggle.addEventListener('click', () => {
    navMenu.classList.add('show-menu')
})
navClose.addEventListener('click', () => {
    navMenu.classList.remove('show-menu')
})