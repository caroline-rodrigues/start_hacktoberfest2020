# LANGUAGE: Ruby
# AUTHOR: Imge
# GITHUB: https://github.com/imgeildan
(0..10).each do |valid_prs|
    if valid_prs >= 4
        puts 'Happy Hacktoberfest'
        break
    else
        puts 'Hello World'
    end
end
