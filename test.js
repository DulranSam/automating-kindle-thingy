if (text.length !== 0) {
    try{
        const jsonData = JSON.parse(text);
        const generatedContent = await generateSubpoints(jsonData, title);
    
        if (Object.keys(generatedContent).length !== 0) {
          theOutcome.push(generatedContent);
          theTitle = title;
          return res.status(200).json({ generatedContent });
        } else {
          return res.status(404).json({ Alert: "No results found!" });
        }
    }catch(err){
        console.error(err);
    }
  } else {
    return res.status(404).json({ alert: "No data retrieved" });
  }