const path = require("path")

exports.onCreatePage = async ({ page, actions }) => {
  const { createPage } = actions
  console.log("Page - " + page.page)
  if (page.path.match(/^\/viewPostLog/)) {
    createPage({
      path: "/viewPostLog",
      matchPath: "/viewPostLog/:id",
      component: path.resolve("src/pages/viewPostLog.js"),
    })
  }
}