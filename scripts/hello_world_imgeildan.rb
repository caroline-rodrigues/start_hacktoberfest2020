# LANGUAGE: Ruby
# AUTHOR: Imge Ildan
# GITHUB: https://github.com/imgeildan

puts 'Hello ' + (Time.now.asctime.include?('Oct') ? 'Hacktoberfest' : 'World')
