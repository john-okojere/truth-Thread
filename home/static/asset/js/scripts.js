document.addEventListener('DOMContentLoaded', function () {
    // Get the nav element
    const navElement = document.getElementById('header');
    const body =  document.querySelector('main')
    // Check if the nav element exists
    if (navElement) {
      // Get the height of the nav element
      const navHeight = navElement.clientHeight + 30 ;

      // Set the body padding to be equal to the nav height
      body.style.paddingTop = navHeight + 'px';
    }
});

function changetab(k) {
    const list = `list-${k}`;
    const navTab =  document.getElementById(list);
    console.log(navTab)
    console.log(list)
    navTab.classList.add('active');
}
const menusicon = document.getElementById('menusicon');
const menus = document.querySelector('.menus ul');
menusicon.innerHTML='<i class="fa fa-bars"></i>';
menusicon.addEventListener('click', () => {
    if(menus.style.display == "none"){
        menus.style.display = "flex";
        menusicon.innerHTML="<i class='fa fa-times'></i>"
    }else{
        menus.style.display = "none";
        menusicon.innerHTML='<i class="fa fa-bars"></i>'
    }
})

