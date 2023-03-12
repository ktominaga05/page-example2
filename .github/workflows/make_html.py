name: learn-github-actions
run-name: ${{ github.actor }} is learning GitHub Actions
on: [push]
jobs:
  make-html:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    permissions:
      contents: 'read'
      id-token: 'write'
      pages: 'write'
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v3
        with:
          python-version: '3.8'
      - name: build
        run: |
          pip install plotly-express
          python make_html.py
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v1
        with:
          # ★★★ Deployするディレクトリ ★★★
          path: 'output'
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@main
 
