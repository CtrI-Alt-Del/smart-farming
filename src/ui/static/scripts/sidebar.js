class Sidebar {
  constructor() {
    this.links = document.querySelectorAll('[data-sidebar-link]')

    if (!this.links.length) return

    const currentUrl = window.location.href

    for (const link of this.links) {
      const slug = link.dataset.sidebarSlug
      if (currentUrl.includes(slug)) {
        link.style.backgroundColor = "#DCFCE7"
        return
      }

      if (slug == 'index' && currentUrl.at(-1) == '/') {
        link.style.backgroundColor = "#FDF6B2"
      }
    }

  }
}


window.addEventListener("load", () => new Sidebar())