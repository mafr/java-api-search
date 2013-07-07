$(function() {
  var dbUrl = "api-index.js";
  var db = [ ];

  var jtypes = {
      "class": "C",
      "interface": "I",
      "enum": "E",
      "annotation": "A",
  }

  function mkDb(rawData) {
      types = $.map(rawData.types, function(val, i) {
          return {
              "jtype": val[0],
              "name": val[1],
              "qname": val[1].toLowerCase(),
              "pkg": val[2],
              "url": val[3],
              "src": val[4],
          }
      });

      db = {
        "apis": rawData.apis,
        "types": types,
      }
  }

  function showError() {
      $("#errorbox").removeClass("hidden");
      $("#msg").text(
          "Cannot read API index file '" + dbUrl + "'. Did you create it?");
  }

  function findMatching(input) {
      input = input.toLowerCase();
      if (input.length == 0)
          return [ ];
      return $.grep(db.types, function(e, i) {
          return e.qname.indexOf(input) == 0; //> 0;
      });
  }

  function mkLink(text, href) {
      return $("<a/>", {
          "href": href,
          "target": "_blank",
      }).text(text);
  }

  function mkRow(item) {
      return $("<tr/>").append(
          $("<td/>").text(jtypes[item.jtype]),
          $("<td/>").append(mkLink(item.name, item.url)),
          $("<td/>").text(item.pkg),
          $("<td/>").text(item.src)
      );
  }

  function go() {
      var results = $("tbody").children();
      if (results.length > 0) {
          window.open(results.find("a").attr("href"), "_blank");
      }
      return false; // prevent submit
  }

  $("#query").bind("keyup", function(event) {
      var input = $("#query").val();
      var result = findMatching(input);

      var tbody = $("tbody").empty();
      for (var i = 0; i < result.length; i++) {
          tbody.append(mkRow(result[i]));
      }
  });

  $("#go").click(go);
  $("form").submit(go);

  $(document).ready(function() {
      $("#query").focus();
      $.getJSON(dbUrl, { }).done(mkDb).error(showError);
  });

});
