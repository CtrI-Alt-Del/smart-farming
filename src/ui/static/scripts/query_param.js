class QueryParam {
  constructor() {
    setTimeout(() => {
      this.updateHtmxUrl()
    }, 2000)
  }

  get(key) {
    const params = new URLSearchParams(document.location.search)
    return params.get(key)
  }

  getAll() {
    const params = new URLSearchParams(document.location.search)
    return Array.from(params)
  }

  append(key, value) {
    const url = new URL(location)
    url.searchParams.set(key, value)
    history.pushState({}, "", url)

    this.updateHtmxUrl()
  }

  remove(key) {
    const url = new URL(window.location.href)
    url.searchParams.delete(key)
    const newUrl = url.search ? url.href : url.href.replace("?", "")
    window.history.replaceState({}, document.title, newUrl)

    this.updateHtmxUrl()
  }

  updateHtmxUrl() {
    const htmxElements = document.querySelectorAll('[data-query-param^="hx-"]')

    if (!htmxElements.length) return

    for (const htmxElement of htmxElements) {
      const htmxMethod = htmxElement.dataset.queryParam
      const htmxUrl = htmxElement.getAttribute(htmxMethod)

      const allParams = this.getAll()

      const params = allParams
        .map((param) => `${param[0]}=${param[1]}`)
        .join("&")

      htmxElement.setAttribute(htmxMethod, `${htmxUrl}?${params}`)

      htmx.process(htmxElement)
    }
  }
}

window.addEventListener("load", () => new QueryParam())
