function copyToClipboard(button) {
    const url = button.parentElement.parentElement
    const url_text = url.querySelector('.url_short').textContent.trim()

    navigator.clipboard
        .writeText(url_text)
        .then(() => {
            butterup.toast({
                message: 'Ссылка скопирована',
                location: 'bottom-center',
                icon: true,
                dismissable: false,
                type: 'success',
            });
        })
}