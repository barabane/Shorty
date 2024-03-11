const modal = document.querySelector('.modal');
const account_btn = document.querySelector('.account_btn')
const modal_close = document.querySelector('.modal_close')

account_btn.addEventListener("click", () => {
    modal.setAttribute("open", "")
})

document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
        modal.removeAttribute("open")
    }
})

modal_close.addEventListener("click", () => {
    modal.removeAttribute("open")
})