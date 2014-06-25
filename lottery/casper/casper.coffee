casper.start 'http://localhost:8081/', ->
  @test.assertExists "input[type=submit]", "Submit button found"
  @test.assertVisible "input[type=submit]", "Submit button is visible"

casper.then testFunc = ->
  @test.assertVisible "input[name=number]", "Number field is visible"
  @fill "form",
    number: '123'
  , true
  @click "input[type=submit]"

  @waitForResource @getCurrentUrl(), ->
    @test.assertSelectorHasText "#result", "you won", "Should be winning"

casper.run()