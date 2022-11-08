// === === == post my imfomation === === === ==
const nav_down = document.getElementById('down'),
    mypost = document.getElementById('mypost'),
    create_a = document.getElementById('create_a'),
    changeup_down = document.getElementById('up_down')

nav_down.addEventListener('click', () => {
    mypost.classList.toggle("show_mypost"),
        create_a.classList.toggle("create_a_show"),
        changeup_down.classList.toggle("down_sow")
});
// =========like on post============
const like = document.getElementById('like'),
    like_change = document.getElementById('like_change')

like.addEventListener('click', () => {
    like_change.classList.toggle('like_change')
});

const emoji = document.getElementById('emoji'),
    emoji_change = document.getElementById('emoji_change')
emoji.addEventListener('click', () => {
    emoji_change.classList.toggle('emoji_change')
});

// =========profile_alls========
const hide_profile_post = document.getElementById('hide_profile_post'),
    profile_alls = document.getElementById('profile_alls')
hide_profile_post.addEventListener('click', () => {
    profile_alls.classList.toggle('profile_all_show')

});

//friends+