#!/usr/bin/env ruby
sender =  ARGV[0].scan(/from:(.\w+)/).join
receiver = ARGV[0].scan(/to:(.\d+)/).join
flags = ARGV[0].scan(/flags:(\S+\d)/).join
puts "#{sender},#{receiver},#{flags}"
