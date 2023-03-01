# 0x16. API advanced

## Resources

**Read or watch**:

- [Reddit API Documentation](https://intranet.alxswe.com/rltoken/b-4nD6hwEeNYTwYl5yWNwA "Reddit API Documentation")
- [Query String](https://intranet.alxswe.com/rltoken/luFn_zrgmAQ0OAO_PEI9bA "Query String")

### General

- How to read API documentation to find the endpoints you’re looking for
    steps:
        - understand purpose of API
        - read documentation overview
        - search fo specific keywords
        - review th available endpoints
        - review the endpoint Documentation
        - experiment with the API
        - troubleshoot

- How to use an API with pagination:
```ANWSER:
        The steps include:
            1. Make an initial request to the API to retrieve the first page of results.
            2. Check the response from the API to see if there are more pages of results available.
            3. If there are more pages available, update the page parameter in your request to retrieve the next page of results.
            4. Repeat steps 2-3 until you have retrieved all the results you need.
```
- How to parse JSON results from an API
 ```   ANSWERS
        the steps include:
               1. Retrieve the JSON data from the API using an HTTP request.
               2. Use a JSON parsing function to convert the JSON data into a usable data structure in your code, such as a dictionary or list.
               3. Access the relevant data in the parsed JSON data structure to use in your application.
```
- How to make a recursive API call
 ```   ANSWERS
        steps:
            1. make intial api request
            2. Process the response
            3. make subsequent requests based on the response until a condition is met.
```
- How to sort a dictionary by value
 ```   ANSWER:
        use `sort()` function to return a lists of paired keys(key-value)
        additionaly use `dictionary()` to convert the sorted lists of the key-value pair
```

## REDIT API elements:
    __Subreddits__: A subreddit is a section of the Reddit website where users can submit and discuss content related to a particular topic.
    __Posts__: Posts are individual pieces of content submitted by users to a subreddit. They can include text, links, images, and videos.
    __Comments__: Comments are responses to posts or other comments, and they can be upvoted or downvoted by other users.
    __Users__: Users are individuals who have created a Reddit account and can submit posts, comments, and upvote or downvote other content.
    __Votes__: Users can vote on content, either upvoting or downvoting it, which affects its visibility on the platform.
    __Messages__: Users can send private messages to each other through the Reddit platform.
    __Moderation__: Subreddits are moderated by a team of moderators who are responsible for enforcing the subreddit's rules and policies. Moderation tools are available through the API for subreddit moderators.
    __Search__: The API allows for searching for specific content or users on the platform.

    Authentication: The Reddit API supports authentication to enable secure access to user data and other features.


