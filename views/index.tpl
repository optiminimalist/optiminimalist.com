#import time

<section class="articlelist">
    #for $id, $article in $articles.items():
        #set $date = $time.strftime("%d %B %Y", $article.date)
        <article class="blogpost">
                    <header class="blog_header">
                      <h1 class="list-title"><a href="/$id">$article.title</a></h1>
                      <span class="date">$date</span>
                <span class="tags">
                [
                #for $t in $article.tags
                  <a href="/tags/$t">\#$t</a>
                #end for
                ]
              </span>
                    </header>
        </article>
    #end for
</section>