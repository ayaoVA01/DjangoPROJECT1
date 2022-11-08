const profile = document.getElementById('my_self'),
    people_list = document.getElementById('people_list'),
    navproflie = document.getElementById('p_img'),
    navBack = document.getElementById('back_icon')


navproflie.addEventListener('click', () => {
    profile.classList.add('show_frofile')
});
navproflie.addEventListener('click', () => {
    people_list.classList.add('peoplelist_remove')
});

navBack.addEventListener('click', () => {
    profile.classList.remove('show_frofile')
});
navBack.addEventListener('click', () => {
    people_list.classList.remove('peoplelist_remove')
});

// ==========show view ==========
const treeIcon = document.getElementById('three'),
    boxList_viwcont = document.getElementById('view_cont'),
    boxview_back = document.getElementById('boxview_back')

treeIcon.addEventListener('click', () => {
    boxList_viwcont.classList.add('view_cont_show'),
        boxList_viwcont.classList.add('view_cont_show li '),
        boxList_viwcont.classList.add('view_cont_show li:hover '),
        boxList_viwcont.classList.add('view_cont_show i:hover ')

});
boxview_back.addEventListener('click', () => {
    boxList_viwcont.classList.remove('view_cont_show')

});