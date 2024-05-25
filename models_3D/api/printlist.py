import json
from curl_cffi import requests

# Define the URL and headers
url = 'https://api.printables.com/graphql/'
headers = {
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'Accept-language': 'en',
    'sec-ch-ua-mobile': '?0',
    'Authorization': '',
    'Client-Uid': '4ac29f0e-26e5-48de-a71d-d3be3290368e',
    'Content-Type': 'application/json',
    'Accept': 'application/json, text/plain, */*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'Referer': 'https://www.printables.com/',
    'operation': 'PrintList',
    'apollographql-client-version': 'v2.100.11',
    'sec-ch-ua-platform': '"Windows"'
}

# Define the GraphQL query
data = {
    "operationName": "PrintList",
    "variables": {
        "limit": 600,
        "categoryId": None,
        "hasMake": False,
        "competitionAwarded": False,
        "featured": False,
        "likedByMe": False,
        "collectedByMe": False,
        "madeByMe": False,
        "ordering": "-likes_count_7_days",
        "publishedDateLimitDays": 30,
        "cursor": None
    },
    "query": """
    query PrintList($limit: Int!, $cursor: String, $categoryId: ID, $materialIds: [Int], $userId: ID, $printerIds: [Int], $licenses: [ID], $ordering: String, $hasModel: Boolean, $filesType: [FilterPrintFilesTypeEnum], $includeUserGcodes: Boolean, $nozzleDiameters: [Float], $weight: IntervalObject, $printDuration: IntervalObject, $publishedDateLimitDays: Int, $featured: Boolean, $featuredNow: Boolean, $usedMaterial: IntervalObject, $hasMake: Boolean, $competitionAwarded: Boolean, $onlyFollowing: Boolean, $collectedByMe: Boolean, $madeByMe: Boolean, $likedByMe: Boolean, $exclusiveFromClubs: Boolean, $paid: PaidEnum, $price: IntervalObject, $verifiedSeller: Boolean, $downloadable: Boolean, $excludedIds: [ID]) {
      morePrints(
        limit: $limit
        cursor: $cursor
        categoryId: $categoryId
        materialIds: $materialIds
        printerIds: $printerIds
        licenses: $licenses
        userId: $userId
        ordering: $ordering
        hasModel: $hasModel
        filesType: $filesType
        nozzleDiameters: $nozzleDiameters
        includeUserGcodes: $includeUserGcodes
        weight: $weight
        printDuration: $printDuration
        publishedDateLimitDays: $publishedDateLimitDays
        featured: $featured
        featuredNow: $featuredNow
        usedMaterial: $usedMaterial
        hasMake: $hasMake
        onlyFollowing: $onlyFollowing
        competitionAwarded: $competitionAwarded
        collectedByMe: $collectedByMe
        madeByMe: $madeByMe
        liked: $likedByMe
        exclusiveFromClubs: $exclusiveFromClubs
        excludedIds: $excludedIds
        paid: $paid
        price: $price
        verifiedSeller: $verifiedSeller
        downloadablePremium: $downloadable
      ) {
        cursor
        items {
          ...PrintListFragment
          __typename
        }
        __typename
      }
    }

    fragment PrintListFragment on PrintType {
      id
      name
      slug
      ratingAvg
      likesCount
      liked
      datePublished
      dateFeatured
      firstPublish
      downloadCount
      category {
        id
        path {
          id
          name
          __typename
        }
        __typename
      }
      modified
      image {
        ...ImageSimpleFragment
        __typename
      }
      nsfw
      premium
      price
      user {
        ...AvatarUserFragment
        __typename
      }
      ...LatestCompetitionResult
      __typename
    }

    fragment AvatarUserFragment on UserType {
      id
      publicUsername
      avatarFilePath
      handle
      company
      verified
      badgesProfileLevel {
        profileLevel
        __typename
      }
      __typename
    }

    fragment LatestCompetitionResult on PrintType {
      latestCompetitionResult {
        placement
        competitionId
        __typename
      }
      __typename
    }

    fragment ImageSimpleFragment on PrintImageType {
      id
      filePath
      rotation
      __typename
    }
    """
}

# Convert the body data dictionary to a JSON string
data_string = json.dumps(data)

r = requests.post(url=url, headers=headers, data=data_string, impersonate='chrome116')
print(r.status_code)

try:
    with open('response.json', 'w') as j:
        json.dump(r.json(), j, indent=2)
except:
    with open('response.txt', 'w', encoding='utf-8') as f:
        f.write(r.json())
finally:
    print(r.status_code)
