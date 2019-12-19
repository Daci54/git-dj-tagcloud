let tagify = new Tagify(taginput, {
    whitelist: [],
    delimiters: "`",
    dropdown : {
        enabled   : 1,
        maxItems  : 20
    }
});

tagify.on('input', onInput)

function onInput( e ){
  let value = e.detail.value;
  tagify.settings.whitelist.length = 0;

  let taginput = {'taginput': value};
  generalAJAX(taginput, "tagquery")
  .then((response) => {
      tagify.settings.whitelist = response.tags;
      tagify.dropdown.show.call(tagify, value);
  })
  .catch((response) => {
      console.log(response);
      console.error('Not receiving Tags from Request');
  })
}